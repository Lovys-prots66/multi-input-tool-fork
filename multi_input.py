from typing import Any

# Pretty prints json using python dicts
def json_form(target: list[dict[str, Any]]):
    # initiate a stringified array with placeholder, perhaps using an f-string would be better?
    out = "[REP\n]"
    dicts = []

    # values that are empty strings show blank value during output, so this guy will place double quotes as default value
    handle_empty_str = lambda x: "\"\"" if x == "" else x

    # wrap each dicts inside curly braces
    for dic in target:
        dict_text = ""
        dict_text += "\n  {"
        # a tab makes 4 spaces tho
        dict_text += ",".join([f'\n\t"{key}": {handle_empty_str(dic[key])}' for key in dic])
        dict_text += "\n  }"
        dicts.append(dict_text)
    # return f"[{','.join(dicts)}\n]" it works the same!
    return out.replace("REP", ",".join(dicts))


def float_range(start: float, stop: float, step=1.0):
    values = [float(start), float(stop), float(step)]
    str_values = [str(start), str(stop), str(step)]
    highest_num = max(map(lambda s: len(s[s.find("."):]), str_values))
    int_values = [int(i * 10 ** (highest_num - 1)) for i in values]
    x = int_values[0]
    if step > 0:
        while x < int_values[1]:
            weird_number = str(x * 10 ** -(highest_num - 1))
            dot_pos = weird_number.find(".") + highest_num
            real_number = float(weird_number[:dot_pos] if dot_pos > 0 else weird_number)
            yield real_number
            x += int_values[2]
    elif step < 0:
        while x > int_values[1]:
            weird_number = str(x * 10 ** -(highest_num - 1))
            dot_pos = weird_number.find(".") + highest_num
            real_number = float(weird_number[:dot_pos] if dot_pos > 0 else weird_number)
            yield real_number
            x += int_values[2]
    else:
        raise ValueError("Step parameter must not be 0")


def add_to_list(target: list[dict]):
    def target_function(func):
        def inner_func(start: float, stop: float, names: list[str], step=1.0):
            count = 0
            for i in float_range(start, stop, step):
                try:
                    new_dict = target[count]
                except IndexError:
                    new_dict = {}
                    target.append(new_dict)
                finally:
                    new_dict[names[0]] = i
                    new_dict[names[1]] = func(i)
                count += 1
            return target
        return inner_func
    return target_function


if __name__ == "__main__":
    results = []

    @add_to_list(results)
    def linear_function(x):
        return 2 * x

    linear_function(0, 4, ["x", "y"], 1)
    print(json_form(results))

