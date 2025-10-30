import { object, string, number, mixed, boolean } from 'yup'

import type { Schema} from 'yup'
import type { IFlatFormValues } from '@features/flatForm'


export const flatSchema: Schema<IFlatFormValues> = object({
    name:    string().required().trim(),
    address: string().required().trim(),

    floor:
        number()
        .typeError('Поле обязательно для заполнения')
        .required()
        .integer()
        .min(-1)
        .when('totalFloors', (tf, schema) =>
            schema.max(typeof tf === 'number' ? tf : Number.MAX_SAFE_INTEGER)
        ),

    totalFloors:
        number()
        .typeError('Поле обязательно для заполнения')
        .required()
        .integer()
        .min(-3)
        .max(200),

    livingSquare:
        number()
        .typeError('Поле обязательно для заполнения')
        .required()
        .integer()
        .min(0),

    kitchenSquare:
        number()
        .typeError('Поле обязательно для заполнения')
        .required()
        .integer()
        .min(0),

    square:
        number()
        .typeError('Поле обязательно для заполнения')
        .required()
        .integer()
        .min(0)
        .max(400)
        .test(
            'square-greater-than-sum',
            'Общая площадь должна быть больше суммы жилой площади и площади кухни',
            function (value) {
                const { livingSquare, kitchenSquare } = this.parent as IFlatFormValues;
                if (value === null || value === undefined) return true;
                const sum = (Number(livingSquare) || 0) + (Number(kitchenSquare) || 0);
                return Number(value) >= sum;
            }
        ),

    heatingType: mixed<'central' | 'gas' | 'electric'>().oneOf(['central', 'gas', 'electric']).required(),
    hasBalcony:  boolean().required(),
});
