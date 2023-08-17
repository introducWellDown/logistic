from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from logic import UserData,generate_id,is_uniq_id,generate_password
from bd_manager import load_client_to_bd

app = FastAPI()

# Пропишем пути к директориям с файлами фронта
static_dir = StaticFiles(directory="../front/static")
templates_dir = '../front/templates/html'

# Подключим статик файлы
app.mount("/static", static_dir, name="static")
# Теперь создадим шаблоны на осонове html страниц
templates = Jinja2Templates(directory=templates_dir)

# GET

@app.get("/")
async def log_in_page(request: Request):
    template = "log_in_page.html"  # Имя вашего HTML файла
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/registration-choice")
async def register_choice_page(request: Request):
    template = "register_choice.html"  # Имя вашего HTML файла
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/register-client")
async def register_client(request: Request):
    template = "register_client.html"  # Имя вашего HTML файла
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/register-worker")
async def register_worker(request: Request):
    template = "register_worker.html"  # Имя вашего HTML файла
    context = {"request": request}
    return templates.TemplateResponse(template, context)

# POST

@app.post("/register-user-successful")
async def register_user(user_data: UserData):
    
    user_data.ID = generate_id()
    _, is_unique = is_uniq_id(user_data.ID,"Users")
    if is_unique:
        user_data.ID = str(is_uniq_id(user_data.ID)[0])
    
    user_data.password = generate_password()
    load_client_to_bd(user_data)
    return {"message": "Registration successful"}
