# SwarmLogic: Your Fluid AI-Powered Backend 

SwarmLogic is an innovative backend solution leveraging swarm intelligence and powered by advanced AI models. It evolves based on API calls, automatically inferring business logic and managing data persistence, saving you from the complexities of traditional backend development.

## Objective

SwarmLogic aims to revolutionize backend development by reducing complexity, saving time, and increasing efficiency. We aim to create a system where backends can evolve based on API calls, automatically inferring business logic, and managing data persistence.

## Architecture

SwarmLogic follows a unique architecture inspired by swarm intelligence. At its core, SwarmLogic utilizes an array of AI agents, each capable of learning and adapting from every API call.

* API Calls: The starting point of our architecture. Any API call triggers our AI swarm.
* AI Swarm: A group of AI agents that interpret the API calls, infer the business logic, and handle the data state.
* Business Logic Inference: Our AI agents use natural language understanding and processing capabilities to understand the purpose of the API call and derive the business logic.
* Data State Management: SwarmLogic automatically manages the data state based on the inferred business logic. It can handle data persistence for different schemas and data sources.

## Getting Started

### Prerequisites

- Python 3.7 or above
- FastAPI
- An OpenAI API key

### Installation

Clone the repository by running the following command in your terminal:

```bash
git clone https://github.com/kyegomez/SwarmLogic.git
```

Once cloned, navigate to the `SwarmLogic` directory:

```bash
cd SwarmLogic
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run the following command in the terminal:

```bash
uvicorn main:app --reload
```

The FastAPI server will start and you can interact with the backend via `http://localhost:8000`.

For API calls, make a POST request to `http://localhost:8000/{app_name}/{api_call}` with a JSON body.

### Example

```bash
curl -X POST "http://localhost:8000/todo_list/create_todo" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"app_name\":\"todo_list\",\"api_call\":\"create_todo\"}"
```

In case of an error or exception, check the `app.log` file in the root directory for detailed information.

## Contributing

We appreciate contributions of any kind and acknowledge them on our README. Please follow the existing coding style, use descriptive commit messages, and remember to test your contributions before submitting a pull request.

## Roadmap

We're dedicated to innovating backend development, and our roadmap is a testament to that. Each phase is a calculated step towards making our vision a reality. To learn more, check out the [roadmap file](docs/ROADMAP.md) file in the root directory.

## License

This project is licensed under the terms of the MIT license. See `LICENSE` for additional details.

## Acknowledgments

A big thank you to our team of researchers, software engineers, and technology enthusiasts committed to innovating and revolutionizing how backends are built. Your hard work is appreciated!

Happy coding!
