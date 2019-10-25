def to_list(sql_output_list):
    """
    [(hog,),(hug,)] => [hog, hug]
    """
    return [sql_column[0] for sql_column in sql_output_list]