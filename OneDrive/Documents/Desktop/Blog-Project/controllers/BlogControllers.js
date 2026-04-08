const Blog = require("../models/Blog");

exports.createBlog = async (req, res) => {
    const data = new Blog(req.body);
    const result = await data.save();
    res.json(result);
};

exports.getBlogs = async (req, res) => {
    const data = await Blog.find();
    res.json(data);
};

exports.getBlogById = async (req, res) => {
    const data = await Blog.findById(req.params.id);
    res.json(data);
};

exports.updateBlog = async (req, res) => {
    const data = await Blog.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.json(data);
};

exports.deleteBlog = async (req, res) => {
    await Blog.findByIdAndDelete(req.params.id);
    res.json({ message: "Blog deleted successfully" });
};  