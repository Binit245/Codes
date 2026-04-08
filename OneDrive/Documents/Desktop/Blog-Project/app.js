console.log("App start ho gya hai");
const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

const blogRoutes = require("./routes/blogRoutes");

const app = express();

app.use(bodyParser.json());

mongoose.connect("mongodb://127.0.0.1:27017/blogDB")
.then(() => console.log("DB Connected"))
.catch((err) => console.log(err));

app.use("/api/blogs", blogRoutes);

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});

