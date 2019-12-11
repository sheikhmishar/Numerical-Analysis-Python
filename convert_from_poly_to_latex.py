ip = get_ipython()
latex_formatter = ip.display_formatter.formatters['text/latex']
latex_formatter.for_type_by_name('numpy.polynomial.polynomial', 'Polynomial', poly2latex)
