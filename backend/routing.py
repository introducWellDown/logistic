from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import logic as lg
import bd_manager

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
    template = "log_in_page.html"  
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/registration-choice")
async def register_choice_page(request: Request):
    template = "register_choice.html"  
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/register-client")
async def register_client(request: Request):
    template = "register_client.html" 
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/register-worker")
async def register_worker(request: Request):
    template = "register_worker.html" 
    context = {"request": request}
    return templates.TemplateResponse(template, context)

# POST

@app.post("/register-user-successful")
async def register_user(user_data: lg.UserData):
    if bd_manager.is_exist_user(user_data) == True:
        print("Пользователь с таким email уже зарегистрирован.")
        return {"status":"error"}

    full_user_data = lg.FullUserData(
        id = lg.generate_id(),
        password= lg.generate_password(),
        last_name= user_data.last_name,
        first_name=user_data.first_name,
        middle_name=user_data.middle_name,
        email=user_data.email,
        company=user_data.company,
        phone=user_data.phone
    )

    bd_manager.load_client_to_bd(full_user_data)
    return {"status":"success","id": full_user_data.id,"password": full_user_data.password}
