#!/bin/zsh

# cal

echo "Calendar"
echo "--------"
cal
# echo "--------"

# weather
echo "Weather"
echo "--------"
wegocmd="/Users/dimpurr/Workflow/00Programing/Go/bin/wego"
$wegocmd -forecast-api-key 0656b207df72ebf3ed8f597c258ed731 -d 0 39.961,116.350  | sed '1,2d'
# echo "--------"

# hold
read -n 1