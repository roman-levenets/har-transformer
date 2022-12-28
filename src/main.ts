import transformationConfig from './transformation.config';
import { LocustTransformer } from './transformers/locust-transformer';

(async () => {
        const transformers = [
            new LocustTransformer(transformationConfig),
        ];

        await Promise.all(transformers.map(item => item.transform()));
    }
)()