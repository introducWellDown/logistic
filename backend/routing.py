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

@app.get("/worker-main-page")
async def worker_main_page(request: Request):
    template = "worker_main_page.html" 
    context = {"request": request}
    return templates.TemplateResponse(template, context)

@app.get("/client-main-page")
async def client_main_page(request: Request):
    template = "client_main_page.html" 
    context = {"request": request}
    return templates.TemplateResponse(template, context)

# POST

@app.post("/register-user-successful")
async def register_user(user_data: lg.UserData):
    if bd_manager.is_exist(user_data,"Users") == True:
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

@app.post("/register-worker-successful")
async def register_worker(worker_data: lg.WorkerData):
    if bd_manager.is_exist(worker_data,"Worker") == True:
        print("Исполнитель с таким email уже зарегистрирован.")
        return {"status":"error"}

    if bd_manager.is_exist_company_code(worker_data) == False:
        print("Код не соответствует компании.")
        return {"status":"error_none_company_code"}
    
    full_woker_data = lg.FullWorkerData(
        id = lg.generate_id(),
        password= lg.generate_password(),
        last_name= worker_data.last_name,
        first_name=worker_data.first_name,
        phone=worker_data.phone,
        email=worker_data.email,
        company=worker_data.company,
        company_code=worker_data.company_code
    )
    
    bd_manager.load_worker_to_bd(full_woker_data)
    return {"status":"success","id": full_woker_data.id,"password": full_woker_data.password}

@app.post("/login")
async def logining(login_data: lg.LoginData):
    user_control_point = bd_manager.logining(login_data,"Users")
    worker_control_point = bd_manager.logining(login_data,"Worker")
    if user_control_point == True:
        return {"status":"success","person":"Client"}
    if worker_control_point == True:
        return {"status":"success","person":"Worker"}
    if (user_control_point and worker_control_point) == False:
        print("Дабл фолс,на вебе должна быть ошибка")
        return {"status":"logining_error"}