import { TransformationConfig } from './core/interfaces';

const config: TransformationConfig = {
    baseUrl: 'https://www.google.com',
    harFilePath: './tests/www.google.com.har',
    outputPath: './tests/',
    authentication: {
        username: 'test-user',
        password: 'test-password'
    }
};

export default config;