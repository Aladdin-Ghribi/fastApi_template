Element	Syntax	When to Use


Headings	          # H1, ## H2, ### H3	       Sections in your README, notes
Bold	              **bold**	                   Emphasize important words
Code block	          ```python ... ```	           Code snippets
Inline code	          `variable`	               Mentioning a function or var
Link	              [text](url)                  References
List	              - item or 1. item	           Steps, todos, features
Checkbox	          - [ ] todo / - [x] done	   Task tracking
Horizontal line	      ---	                       Separating sections





- ### setup uv repo

`uv init <folder_name>`


- ### starting dependencies 

```python 
uv add fastapi "uvicorn[standard]" sqlalchemy databases pydantic pydantic-settings httpx
uv add --dev pytest black ruff
```

- ### everyday workflow checking 

```python
uv run ruff check .
uv run black . 
uv run pytest
```


- ### database commands 
##### async driver for postgresql
`uv add asyncpg` 



### note
we are includind dockers in this template for modern integrations and better development experience 




### testing details and notes for future work 


- **A simple reusable checklist for future routes:**

1. Arrange: prepare client and any needed data.
2. Act: call the endpoint.
3. Assert: check status, body, and only the important contract fields.
4. Isolate: mock or control config, DB, or external APIs when needed.