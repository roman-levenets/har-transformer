import fs from 'fs';
import path from 'path';
import { TransformationConfig } from './interfaces';
import { HarParser } from './har-parser';
import transformationConfig from '../transformation.config';

export abstract class BaseTransformer {
    protected readonly parser: HarParser;

    protected constructor(protected readonly config: TransformationConfig) {
        this.parser = new HarParser(this.config);
    }

    abstract get transformerName(): string;

    abstract transform(): void;

    protected writeContentsToFile(fileName: string, contents: string): Promise<void> {
        const directoryPath = path.join(transformationConfig.outputPath, `${this.transformerName}`);
        const filePath = path.join(directoryPath, fileName);

        if (!fs.existsSync(directoryPath)) {
            fs.mkdirSync(directoryPath, { recursive: true });
        }

        return new Promise<void>((resolve, reject) => {
            fs.writeFile(filePath, contents, { flag: 'w', encoding: 'utf-8' }, (err) => {
                if (err) {
                    reject(err);
                    throw err;
                }

                resolve();
            });
        });
    }
}