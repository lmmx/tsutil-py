(function_definition
  parameters: (parameters
    (_) @param
    (#match? @param "^[^*]") ; Exclude *args and **kwargs
    (#match? @param "^[^/]") ; Exclude / for keyword-only arguments
  )
  (#match? @param ".{8,}")) ; Match if there are 8 or more parameters
