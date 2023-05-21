# RapidExec (Work in progress)

RapidExec is a command line tool that allows you to easier access docker containers. It is written in Python and uses the docker API to interact with the containers.


## Installation

To install RapidExec, you can use pip:

```bash
pip install rapidexec
```

## Usage

To use RapidExec, you can use the following command:

```bash
rapidexec [OPTIONS] COMMAND [ARGS]...
```

### Options

| Option | Description |
| ------ | ----------- |
| --help | Show this message and exit. |
| --version | Show the version and exit. |
| --config PATH | Path to the config file. |
| --debug | Enable debug mode. |

### Commands

| Command | Description |
| ------- | ----------- |
| add | Add a new container to the config file. |
| list | List all containers. |
| remove | Remove a container from the config file. |
| run | Run a command in a container. |
| start | Start a container. |
| stop | Stop a container. |
| update | Update a container in the config file. |
| docker-ps | List all running containers. |
| docker-rm | Remove a container. |
| docker-run | Run a command in a container. |
| docker-start | Start a container. |
| docker-stop | Stop a container. |


### Example output

```bash
$ rapidexec docker-ps
```
![image](https://github.com/godd0t/rapidexec/assets/58993673/1f7847c3-73cc-42ab-97da-2698aa1387a5)

## Config file

The config file is a JSON file that contains all the containers that you want to use with RapidExec. The default location of the config file is `~/.config/rapidexec/config.json`. You can change the location of the config file with the `--config` option.

### Example

```json
{
    "containers": [
        {
            "name": "nginx",
            "image": "nginx:latest",
            "command": "nginx -g 'daemon off;'",
            "ports": [
                {
                    "host": 80,
                    "container": 80
                }
            ]
        }
    ]
}
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contributing

If you want to contribute to this project, you can create a pull request on GitHub.
