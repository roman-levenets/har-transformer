export interface TransformationConfig {
    baseUrl: string;
    harFilePath: string;
    outputPath: string;
    authentication: {
        username: string;
        password: string
    }
}

export type HttpMethod = 'GET' | 'POST' | 'PUT';

export interface UrlInfo {
    url: string;
    method: HttpMethod;
    body?: any;
}