import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT category,
SUM(quantity * price) AS sales
FROM orders
GROUP BY category