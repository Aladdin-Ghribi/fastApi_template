# FastAPI template 
### modern files structure uv package manager based configuration 

#### **key stracture details:**


- basic modular db structure
- core folder for .env secure access and logging basic console format
- testing with simple sync client access
- ready to activate docker compose file for postgresql secure container access
- initial basic dependencies and dev tools
- modern app-api version based strucutre with prefix notation


#### **simple cloning commands**
1. 
```python
git clone https://github.com/Aladdin-Ghribi/fastApi_template.git
cd fastApi_template
uv sync
docker compose up -d
.\.venv\Scripts\activate.ps1
```
2. create your own .env file with .env.example 

3. `uv run uvicorn app.main:app --reload`




### and you good to go with your application :)
