import { TransformationConfig } from '../core/interfaces';
import { BaseTransformer } from '../core/base-transformer';

export class LocustTransformer extends BaseTransformer {
    constructor(config: TransformationConfig) {
        super(config);
    }

    get transformerName(): string {
        return 'locust-transformer';
    }

    async transform(): Promise<void> {
        const urlList = this.parser.getRequestUrls();

        let scriptContents = `from locust import HttpUser, task, events, between, LoadTestShape
import gevent
import json
import greenlet
import random
from datetime import datetime, timedelta
import math


class LoadTestScenario(HttpUser):
    wait_time = between(1, 5)
    test_data = {}
    v_user_list = dict()
    current_v_user_row = int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.client.auth = ('${this.config.authentication.username}', '${this.config.authentication.password}')

    @events.init.add_listener
    def on_locust_init(environment, **kwargs):
        LoadTestScenario.load_test_data()

    @task
    def test_task(self):
        v_user_id = greenlet.getcurrent().minimal_ident

        max_v_user_row = max(LoadTestScenario.v_user_list.values(), default=-1)
        LoadTestScenario.v_user_list[v_user_id] = max_v_user_row + 1
        self.current_v_user_row = LoadTestScenario.v_user_list[v_user_id]

        self.execute_local_requests()
        self.execute_remote_requests()`;

        let localRequestsContents = `
    def execute_local_requests(self):`;

        let remoteRequestsContents = `
    def execute_remote_requests(self):`;

        urlList.forEach(urlInfo => {
            const relativeUrl = this.parser.getRelativeUrl(urlInfo.url);
            const method = urlInfo.method.toLowerCase();
            const padding = ''.padStart(4);
            const doublePadding = ''.padStart(8);

            const body = urlInfo.method === 'POST' || urlInfo.method === 'PUT'
                ? `,\n${doublePadding}${padding}json=${JSON.stringify(urlInfo.body)}`
                : '';

            if (relativeUrl !== urlInfo.url) {
                localRequestsContents += `\n${doublePadding}self.client.${method}('${relativeUrl}'${body})`.padStart(4);
            } else {
                remoteRequestsContents += `\n${doublePadding}self.client.${method}('${urlInfo.url}'${body})`;
            }
        });

        scriptContents += `\n${localRequestsContents}`;
        scriptContents += `\n${remoteRequestsContents}`;

        scriptContents += `\n
    @staticmethod
    def load_test_data():
        with open('data.json') as data_file:
            LoadTestScenario.test_data = json.load(data_file)\n`;

        scriptContents += `${this.addLoadTestShape()}\n`;

        await this.writeContentsToFile('locustfile.py', scriptContents);
    }

    private addLoadTestShape(): string {
        return `
    class StagesShape(LoadTestShape):
        """
        A step load shape
        Keyword arguments:
            step_time -- Time between steps
            step_load -- User increase amount at each step
            spawn_rate -- Users to stop/start per second at every step
            time_limit -- Time limit in seconds
        """

        step_time = 300
        step_load = 5
        spawn_rate = 5
        time_limit = 3600

        def tick(self):
            run_time = self.get_run_time()

            if run_time > self.time_limit:
                return None

            current_step = math.floor(run_time / self.step_time) + 1
            return (current_step * self.step_load, self.spawn_rate)`;
    }
}