import { TransformationConfig } from './core/interfaces';

const config: TransformationConfig = {
    baseUrl: 'https://www.google.com',
    harFilePath: './tests/1-test-scenario/www.google.com.har',
    outputPath: './tests/1-test-scenario/',
    authentication: {
        username: 'test-user',
        password: 'test-password'
    }
};

export default config;