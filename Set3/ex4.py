def build_xml_element(tag, content, **attributes):
    """Builds and returns a string representing an XML element.
    Since some XML/HTML attribute names are Python reserved words
    (e.g. "class"), those keyword arguments are passed with a leading
    underscore (e.g. _class="my-link") and the underscore is stripped
    when building the final attribute name."""
    attr_parts = []
    for name, value in attributes.items():
        clean_name = name.lstrip("_")
        attr_parts.append(f'{clean_name}="{value}"')

    attrs_str = " ".join(attr_parts)
    if attrs_str:
        return f"<{tag} {attrs_str}>{content}</{tag}>"
    return f"<{tag}>{content}</{tag}>"


if __name__ == "__main__":
    print(build_xml_element(
        "a", "Hello there",
        href="http://python.org", _class="my-link", id="someid"))
    # <a href="http://python.org" class="my-link" id="someid">Hello there</a>
