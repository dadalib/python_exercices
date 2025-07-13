def CheckDOM(strParam):
    allowed_tags = {"b", "i", "em", "div", "p"}
    tags = []
    i = 0

    try:
        while i < len(strParam):
            if strParam[i] == "<":
                j = i + 1
                is_close = False

                if j >= len(strParam):
                    return False

                if strParam[j] == "/":
                    is_close = True
                    j += 1

                tag_name = ""
                while j < len(strParam) and strParam[j] != ">":
                    tag_name += strParam[j]
                    j += 1

                if tag_name not in allowed_tags:
                    raise ValueError(f"Invalid tag detected: {tag_name}")

                if not is_close:
                    tags.append(tag_name)
                else:
                    if tags and tags[-1] == tag_name:
                        tags.pop()
                    else:
                        if tags:
                            return tags[-1]
                        else:
                            return tag_name  # Return the unmatched closing tag

                i = j  # move to '>'
            i += 1

        if not tags:
            return True
        elif len(tags) == 1:
            return tags[0]
        else:
            return False
    except Exception as error:
        print("Fatal error parsing:", error)
        return False

if __name__ == "__main__":
    # Use the test string directly for clarity
    test_input = "<div><b><p>hello world</p></b></div>"
    result = CheckDOM(test_input)
    print(result)

