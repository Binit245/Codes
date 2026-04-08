const mongoose = require("mongoose");

const blogschema = new mongoose.Schema({
    blog: String,
    author: String,
    rating: Number
});

module.exports = mongoose.model("Blog", blogschema);