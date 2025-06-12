# ModuLearn

ModuLearn is a demo project for building AI-generated micro-curriculums for underserved schools.

## Structure

- `generator/` – Python module that handles AI-based curriculum generation.
- `frontend/` – Streamlit interface for teachers to request a learning module.
- `data/` – Sample data and outputs.
- `docs/` – Documentation on standards and design notes.

## Running

Install the requirements and launch the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run frontend/app.py
```

The generator uses the OpenAI API. Set the environment variable `OPENAI_API_KEY` with your key before running.

## License

MIT
