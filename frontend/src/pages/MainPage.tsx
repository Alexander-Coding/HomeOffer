import Paper from '@mui/material/Paper'

import { FlatForm } from "@features"
import { MainPageLayout } from "@layouts"


export const MainPage = () => {
    return (
        <Paper elevation={2}>
            <MainPageLayout title="Форма объекта недвижимости">
                <FlatForm />
            </MainPageLayout>
        </Paper>
    );
}