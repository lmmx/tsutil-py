(function_definition
  body: (block
    (expression_statement)+) @function_body
  (#match? @function_body "^.{300,}$"))

(lambda
  body: (_) @lambda_body
  (#match? @lambda_body "^.{100,}$"))
