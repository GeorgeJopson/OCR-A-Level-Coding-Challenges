const express = require('express');
const bodyParser = require('body-parser');
const ejs = require('ejs');
const mongoose = require('mongoose');

app=express();

app.use(express.static('public'));
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended:true}));

mongoose.connect("mongodb://localhost:27017/rockClimbingDB",{useNewUrlParser:true,useUnifiedTopology:true})

const memberSchema = new mongoose.Schema({
  fName:{
    type:String,
    required:true
  },
  lName:{
    type:String,
    required:true
  },
  email:{
    type:String,
    required:true
  }
})

const Member = mongoose.model("Member",memberSchema);

app.get("/",function(req,res){
  res.render("home")
});
app.get("/register",function(req,res){
  res.render("register")
})
app.get("/seeUsers",function(req,res){
  Member.find({},function(err,members){
    res.render("seeUsers",{members:members});
  });
});
app.post("/register",function(req,res){
  let fName = req.body.fName;
  let lName = req.body.lName;
  let email = req.body.email;
  res.render("confirm",{fName:fName,lName:lName,email:email})
});
app.post("/confirm",function(req,res){
  const newMember= Member({
    fName:req.body.fName,
    lName:req.body.lName,
    email:req.body.email
  });
  newMember.save(function(err){
    if(err){
      console.log(err);
    }else{
      res.redirect("/");
    }
  });
})
app.listen(3000)
