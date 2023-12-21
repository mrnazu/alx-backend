const express = require('express');
const app = express();

const allItems = Array.from({ length: 50 }, (_, index) => `Item ${index + 1}`);

app.get('/items', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const pageSize = 10;
  const startIndex = (page - 1) * pageSize;
  const endIndex = startIndex + pageSize;
  const itemsOnPage = allItems.slice(startIndex, endIndex);

  setTimeout(() => {
    res.json({
      items: itemsOnPage,
      currentPage: page,
      totalPages: Math.ceil(allItems.length / pageSize)
    });
  }, 500);
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});
