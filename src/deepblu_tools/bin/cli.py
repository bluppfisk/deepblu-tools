#! /usr/bin/env python3

###
# Deepblu Backup Tool
# by Sander Van de Moortel
#
# https://github.com/bluppfisk/deepblu-tools
#
# Connects to Deepblu and backs up dives in UDDF format
# See http://uddf.org for more information on the format
#

import json
import sys

import click
import requests
from deepblu_tools import deepblu_api as api
from deepblu_tools.models import deepblu as dm
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def load_posts_from_file(infile: str) -> dict:
    try:
        with open(infile, "r") as fp:
            return json.load(fp)
    except Exception as e:
        click.echo(f"Could not open infile {infile}: {e}", err=True)


def load_posts_from_api(deepblu_user: dm.DeepbluUser, with_drafts: bool) -> dict:
    click.echo("Getting published logs")
    published_posts = api.load_dives(deepblu_user, post_type="published")
    draft_posts = []

    if with_drafts:
        click.echo("Getting draft logs for logged in user")
        draft_posts = api.load_dives(deepblu_user, post_type="draft")

    return published_posts + draft_posts


@click.command()
@click.option(
    "-f",
    "--infile",
    help="For debugging purposes: load data from JSON file instead of API",
    required=False,
)
@click.option("-u", "--user", help="Deepblu username or userid", required=False)
@click.option("-p", "--password", help="Deepblu password", required=False)
@click.option(
    "-m", "--max-logs", help="Maximum number of logs to parse", required=False, type=int
)
@click.option(
    "-d",
    "--with-drafts",
    help="Also pull draft logs. Requires valid credentials",
    type=bool,
    is_flag=True,
)
@click.option("-o", "--outfile", help="Write results to this file", type=str)
def main(
    user: str,
    password: str,
    max_logs: int,
    with_drafts: bool,
    outfile: str,
    infile: str,
):
    if not user and not infile:
        raise click.BadArgumentUsage("Specify at least a user id, an infile or an email and password combination")
    try:
        deepblu_user = api.login(user, password)
    except requests.exceptions.HTTPError as e:
        click.echo(e.response.status_code)
        error_message = e.response.json().get("message")
        click.echo("Deepblu replied: " + error_message)
        exit(int(e.response.status_code))

    if not deepblu_user.logged_in:
        # get data from API without logging in
        # may fail if Deepblu ever restrict access
        click.echo("Attempting to access API without logging in... (experimental)")

        if with_drafts:
            click.echo("Cannot get drafts if user is not logged in")
            with_drafts = False

    posts = []
    if infile:
        posts = load_posts_from_file(infile)
    else:
        posts = load_posts_from_api(deepblu_user, with_drafts=with_drafts)

    if not posts:
        if deepblu_user.logged_in:
            raise click.ClickException("No posts found on this account")
        else:
            raise click.ClickException(
                "Either this account has no posts or could not be retrieved anonymously with this user id"
            )

    logbook = dm.DeepbluLogBook(posts, deepblu_user, max_posts=max_logs)
    uddf = logbook.to_uddf()
    config = SerializerConfig(pretty_print=True)

    try:
        fp = sys.stdout
        if outfile:
            fp = open(outfile, "w+")

        fp.write(
            XmlSerializer(config=config).render(
                uddf, ns_map={None: "http://www.streit.cc/uddf/3.2/"}
            )
        )
    except BrokenPipeError:
        pass
    except Exception as e:
        raise click.ClickException("Could not write to file", e)


if __name__ == "__main__":
    main()
