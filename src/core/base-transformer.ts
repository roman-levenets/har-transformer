import { TransformationConfig } from './interfaces';
import { HarParser } from './har-parser';
import { writeFileSync } from 'fs';
import { join } from 'path';
import transformationConfig from '../transformation.config';

export abstract class BaseTransformer {
    protected readonly parser: HarParser;

    protected constructor(protected readonly config: TransformationConfig) {
        this.parser = new HarParser(this.config);
    }

    abstract transform(): void;

    protected writeContentsToFile(contents: string, fileName: string): void {
        writeFileSync(join(transformationConfig.outputPath, fileName), contents, {
            flag: 'w',
        });
    }
}