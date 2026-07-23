import datetime
import copy
import urllib.parse
from typing import Sequence

import dominate.tags



def is_tumblr_url(url: str | urllib.parse.ParseResult):
    """Checks URL is a tumblr URL"""
    if isinstance(url, str):
        if "tumblr.com" not in url:
            return False
        url = urllib.parse.urlparse(url)
    elif not isinstance(url, urllib.parse.ParseResult):
        return False

    hostname = url.hostname
    if hostname and (hostname == "tumblr.com" or hostname.endswith(".tumblr.com")):
        return True
    return False


def url_handler(url: str | urllib.parse.ParseResult):
    """Change URLs found in posts to privacy-friendly alternatives"""
    # ponytail: fast string matching for standard Tumblr URLs -> fallback to urlparse for complex/query redirects
    if isinstance(url, str):
        if url.startswith("/"):
            return url
        if "href.li" in url or "t.umblr.com" in url:
            url_obj = urllib.parse.urlparse(url)
            hostname = url_obj.hostname or ""
            try:
                if hostname.endswith("href.li"):
                    return url_handler(url_obj.query)
                elif hostname.endswith("t.umblr.com"):
                    parsed_query = urllib.parse.parse_qs(url_obj.query)
                    if redirect_url := parsed_query.get("z"):
                        return url_handler(redirect_url[0])
            except AttributeError:
                pass
            url = url_obj
        elif "tumblr.com" in url:
            # Fast path without full urlparse
            scheme_end = url.find("://")
            if scheme_end != -1:
                after_scheme = url[scheme_end + 3:]
                slash_pos = after_scheme.find("/")
                if slash_pos != -1:
                    hostname = after_scheme[:slash_pos]
                    path = after_scheme[slash_pos:]
                else:
                    hostname = after_scheme
                    path = ""

                if hostname.endswith(".media.tumblr.com"):
                    sub_domains = hostname.split(".")
                    if sub_domains[1] == "media":
                        return f"/tblr/media/{sub_domains[0]}{path}"
                    elif sub_domains[0] == "www" and sub_domains[2] == "media":
                        return f"/tblr/media/{sub_domains[1]}{path}"
                elif hostname.endswith("assets.tumblr.com"):
                    return f"/tblr/assets{path}"
                elif hostname.endswith("static.tumblr.com"):
                    return f"/tblr/static{path}"
                elif hostname.startswith("a."):
                    return f"/tblr/a{path}"
                elif hostname.endswith("tumblr.com"):
                    sub_domains = hostname.split(".")
                    potential_blog_name = sub_domains[1] if sub_domains[0] == "www" else sub_domains[0]
                    if potential_blog_name != "tumblr":
                        if path.startswith("/post"):
                            return f"/{potential_blog_name}{path[5:]}"
                        else:
                            return f"/{potential_blog_name}{path}"
                    else:
                        return path
            url = urllib.parse.urlparse(url)
        else:
            return url
    elif not isinstance(url, urllib.parse.ParseResult):
        raise ValueError

    hostname = url.hostname or ""

    try:
        if hostname.endswith("href.li"):
            return url_handler(url.query)
        elif hostname.endswith("t.umblr.com"):
            parsed_query = urllib.parse.parse_qs(url.query)
            if redirect_url := parsed_query.get("z"):
                return url_handler(redirect_url[0])
    except AttributeError:
        pass

    if hostname.endswith("tumblr.com"):
        if hostname.endswith(".media.tumblr.com"):
            sub_domains = hostname.split(".")
            if sub_domains[1] == "media":
                return f"/tblr/media/{sub_domains[0]}{url.path}"
            elif sub_domains[0] == "www" and sub_domains[2] == "media":
                return f"/tblr/media/{sub_domains[1]}{url.path}"

        if hostname.endswith("assets.tumblr.com"):
            return f"/tblr/assets{url.path}"
        elif hostname.endswith("static.tumblr.com"):
            return f"/tblr/static{url.path}"
        elif hostname.startswith("a."):
            return f"/tblr/a{url.path}"
        else:
            sub_domains = hostname.split(".")
            potential_blog_name = sub_domains[1] if sub_domains[0] == "www" else sub_domains[0]

            if potential_blog_name != "tumblr":
                if url.path.startswith("/post"):
                    return f"/{potential_blog_name}{url.path[5:]}"
                else:
                    return f"/{potential_blog_name}{url.path}"
            else:
                return f"{url.path}"

    return url.geturl()


def create_reblog_attribution_link(post):
    """Creates an attribution of who the author reblogged the post from"""
    reblog_from_url = urllib.parse.urlparse(post.reblog_from.post_url)
    reblog_attribution_element_classes = ["link", "blog-name"]

    if post.reblog_from.blog_name:
        reblogged_from_name = post.reblog_from.blog_name
    else:
        reblogged_from_name = "reblogged"
        reblog_attribution_element_classes.append("hidden-reblog")

    if not is_tumblr_url(reblog_from_url):
        if (post.reblog_root.post_id == post.reblog_from.post_id) and post.reblog_root.blog_name:
            reblog_from_url = f"/{post.reblog_root.blog_name}/{post.reblog_from.id}"
        else:
            return dominate.tags.span(reblogged_from_name, cls="blog-name hidden-reblog")

    return dominate.tags.a(
        reblogged_from_name,
        href=url_handler(reblog_from_url),
        cls=" ".join(reblog_attribution_element_classes),
    )


def update_query_params(base_query_args, key, value=None):
    """Returns a URL query string with a parameter replaced/added"""
    if isinstance(base_query_args, str):
        base_query_args = urllib.parse.parse_qs(base_query_args)
    else:
        try:
            base_query_args = dict(base_query_args)
        except Exception:
            base_query_args = base_query_args.copy() if hasattr(base_query_args, "copy") else copy.copy(base_query_args)

    if isinstance(key, dict):
        for k, v in key.items():
            if isinstance(v, (list, tuple)):
                base_query_args[k] = v
            else:
                base_query_args[k] = [v]
    else:
        if isinstance(value, (list, tuple)):
            base_query_args[key] = value
        else:
            base_query_args[key] = [value]

    return urllib.parse.urlencode(base_query_args, doseq=True)


def remove_query_params(base_query_args, key):
    """Returns a URL query string with a parameter replaced/added"""
    base_query_args = base_query_args.copy() if hasattr(base_query_args, "copy") else copy.copy(base_query_args)

    if base_query_args.get(key):
        del base_query_args[key]

    return urllib.parse.urlencode(base_query_args, doseq=True)


def deseq_urlencode(query_args):
    return urllib.parse.urlencode(query_args, doseq=True)


def prefix_slash_in_url_if_missing(url):
    if not url.startswith("/"):
        return f"/{url}"
    return url



async def create_poll_callback(ctx, blog, post_id):
    async def poll_callable(poll_id, expiration_timestamp):
        current_timestamp = round(datetime.datetime.utcnow().timestamp())
        expired = current_timestamp > expiration_timestamp

        initial_results = await ctx.TumblrAPI.poll_results(blog, post_id, poll_id)
        return initial_results["response"]

    return poll_callable
