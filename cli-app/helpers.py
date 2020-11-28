import click


def get_filename(response):
    """
    Get filename from a response

    :param response: Response
    :return: string
    """
    import re
    return re.findall("filename=\"(.+)\"", response.headers['content-disposition'])[0]


def store_file(file_name, response):
    """
    Store a file locally.

    :param file_name: string
    :param response: Response
    :return: False
    """
    with open(file_name, 'wb') as file:
        file.write(response.content)
        click.echo(f'{file_name} saved successfully.')


def handle_file_response(response):
    """
    Handles a response containing files.

    :param response: Response
    :return: False
    """
    if response.status_code == 200:
        file = get_filename(response)
        store_file(file, response)
    else:
        click.echo(response.json())
