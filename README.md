# ResearchMind

ResearchMind is a multi-agent AI research assistant built with Python, LangChain, and Streamlit. It helps users explore a topic by:

- searching the web for recent, relevant information,
- selecting and scraping a high-value source,
- writing a structured research report,
- reviewing the final draft with a critic-style evaluation.

The project is designed as an interactive web app, with the same research workflow also available from a simple Python script.

## Features

- Web search via Tavily
- URL scraping and text extraction via BeautifulSoup and requests
- LLM-powered research agents and writing pipeline
- Critic chain that scores and improves the final report
- Streamlit interface for a polished user experience
- Downloadable Markdown report output

## Project structure

```text
.
├── agents.py          # LLM setup, agent builders, and prompt chains
├── app.py             # Streamlit front-end UI
├── pipeline.py        # CLI version of the research workflow
├── tools.py           # Search and scraping tools used by agents
├── requirements.txt   # Python dependencies
├── .env               # Local environment variables (not committed in some setups)
└── README.md          # Project documentation
```

## Tech stack

- Python 3.10+
- LangChain
- Streamlit
- Tavily Search API
- BeautifulSoup
- requests
- Groq/OpenAI/Google GenAI models via LangChain integrations

## Prerequisites

Before running the app, install the required dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

You also need API keys for the services used by the pipeline:

- `TAVILY_API_KEY` for the search tool
- a model provider key such as `GROQ_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_API_KEY`

Create a `.env` file in the project root with values like:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

If you want to use a different model provider, update the configuration in `agents.py` accordingly.

## Running the app

Start the Streamlit interface from the project root:

```bash
streamlit run app.py
```

Then:

1. enter a research topic,
2. click the run button,
3. review the search results, scraped content, final report, and critic feedback,
4. download the generated report as a Markdown file.

## Running the pipeline from the terminal

You can also run the research flow directly in a terminal:

```bash
python pipeline.py
```

This will prompt for a topic and execute the same multi-step workflow without the UI.

## How the workflow works

The app uses a four-stage agent pipeline:

1. Search Agent
   - queries the web for recent and relevant sources
2. Reader Agent
   - picks the strongest result and scrapes its content
3. Writer Chain
   - turns the gathered research into a structured report
4. Critic Chain
   - reviews the report and gives a score plus feedback

## Notes

- The agent setup is configurable in `agents.py`.
- The current default model configuration uses Groq with `openai/gpt-oss-120b`.
- The project is intentionally lightweight and suitable for experimentation or extending into a richer research workflow.

## License

This project does not include a license file. If you plan to share or distribute it, add an appropriate open-source license before publishing.
