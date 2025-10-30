// Интерфейс для значений формы данных о квартире
export interface IFlatFormValues {
    name:          string;       // Название объекта
    address:       string;       // Адрес объекта
    floor:         number | '';  // Этаж
    totalFloors:   number | '';  // Всего этажей в доме
    square:        number | '';  // Общая площадь
    livingSquare:  number | '';  // Жилая площадь
    kitchenSquare: number | '';  // Площадь кухни
}