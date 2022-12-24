import transformationConfig from './transformation.config';
import { LocustTransformer } from './transformers/locust-transformer';

const transformer = new LocustTransformer(transformationConfig);
transformer.transform();