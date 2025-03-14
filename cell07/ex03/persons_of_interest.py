def famous_births(figures_dict):
    # เรียงลำดับบุคคลตามวันเกิดและแสดงผล
    sorted_figures = sorted(figures_dict.items(), key=lambda item: item[1]['date_of_birth'])
    for key, figure_info in sorted_figures:
        print(f"{figure_info['name']} is a great scientist born in {figure_info['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)