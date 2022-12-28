import fs from 'fs';
import { TransformationConfig, UrlInfo } from './interfaces';

export class HarParser {
    constructor(private readonly config: TransformationConfig) {
    }

    getRequestUrls(): UrlInfo[] {
        const harData = this.getHarData();
        const entries = harData.log.entries as any[];
        return entries.filter(item => !!item.request?.url).map(item => ({
            url: item.request.url as string,
            method: item.request.method,
            body: JSON.parse(item.request.postData?.text || '{}')
        }));
    }

    getRelativeUrl(url: string): string {
        const pattern = `^${this.config.baseUrl}`;
        return url.replace(new RegExp(pattern), '');
    }

    private getHarData(): any {
        const harDataContents = fs.readFileSync(this.config.harFilePath, 'utf-8');
        return JSON.parse(harDataContents);
    }
}