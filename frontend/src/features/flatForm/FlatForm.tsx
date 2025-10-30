import React from 'react';
import { Formik, Form } from 'formik';

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

import { flatSchema } from './schema';
import { flatFormInitialValues } from './static';
import { TextFieldField, CheckboxField, RadioGroupField } from './adapters';

import type { IFlatFormValues } from './types';

export const FlatForm: React.FC = () => {
    return (
        <Formik<IFlatFormValues>
            initialValues={flatFormInitialValues}
            validationSchema={flatSchema}
            onSubmit={(values) => {
                const normalized = {
                    ...values,
                    floor: Number(values.floor),
                    totalFloors: Number(values.totalFloors),
                    square: Number(values.square),
                    livingSquare: Number(values.livingSquare),
                    kitchenSquare: Number(values.kitchenSquare),
                };
                console.log('Submit:', normalized);
                alert('Форма валидна. Смотрите консоль.');
            }}
            validateOnBlur
            validateOnChange
        >
            {() => (
                <Form noValidate>
                    <Stack spacing={2}>
                        <TextFieldField name="name" label="Название объекта" fullWidth />

                        <TextFieldField name="address" label="Адрес" fullWidth />

                        <TextFieldField
                            name="floor"
                            label="Этаж"
                            type="number"
                            fullWidth
                            slotProps={{ htmlInput: { inputMode: 'numeric', pattern: '[0-9-]*' } }}
                        />

                        <TextFieldField
                            name="totalFloors"
                            label="Количество этажей в доме"
                            type="number"
                            fullWidth
                            slotProps={{ htmlInput: { inputMode: 'numeric', pattern: '[0-9-]*' } }}
                        />

                        <TextFieldField
                            name="square"
                            label="Площадь"
                            type="number"
                            fullWidth
                        />

                        <TextFieldField
                            name="livingSquare"
                            label="Жилая площадь"
                            type="number"
                            fullWidth
                        />

                        <TextFieldField
                            name="kitchenSquare"
                            label="Площадь кухни"
                            type="number"
                            fullWidth
                        />

                        <RadioGroupField
                            name="heatingType"
                            label="Тип отопления"
                            options={[
                                { label: 'Центральное', value: 'central' },
                                { label: 'Газовое', value: 'gas' },
                                { label: 'Электрическое', value: 'electric' },
                            ]}
                            row={false}
                        />

                        <CheckboxField name="hasBalcony" label="Балкон" />

                        <Box mt={1} display="flex" gap={2}>
                            <Button type="submit" variant="contained">
                                Сохранить
                            </Button>
                            <Button type="reset" variant="outlined">
                                Сбросить
                            </Button>
                        </Box>
                    </Stack>
                </Form>
            )}
        </Formik>
    );
};