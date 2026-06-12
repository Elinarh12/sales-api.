import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT product,
SUM(quantity) AS total
FROM orders
GROUP BY product
ORDER BY total DESC
LIMIT 5