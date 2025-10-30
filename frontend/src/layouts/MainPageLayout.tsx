import Box from '@mui/material/Box'
import Container from '@mui/material/Container'
import Typography from '@mui/material/Typography'
import AppBar from '@mui/material/AppBar'
import Toolbar from '@mui/material/Toolbar'

import type { FC } from 'react'
import type { IMainPageLayoutProps } from '@layouts'


export const MainPageLayout: FC<IMainPageLayoutProps> = ({ children, title = 'Приложение' }) => {
    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
            {/* Header */}
            <AppBar position="static" elevation={1}>
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        {title}
                    </Typography>
                </Toolbar>
            </AppBar>

            {/* Main content */}
            <Box component="main" sx={{ flexGrow: 1, py: 4, bgcolor: 'grey.50' }}>
                <Container maxWidth={'sm'}>
                    {children}
                </Container>
            </Box>

            {/* Footer */}
            <Box
                component="footer"
                sx={{
                    py: 2,
                    px: 2,
                    mt: 'auto',
                    bgcolor: 'grey.200',
                    textAlign: 'center',
                }}
            >
                <Typography variant="body2" color="text.secondary">
                    © {new Date().getFullYear()} Тестовое задание
                </Typography>
            </Box>
        </Box>
    );
};