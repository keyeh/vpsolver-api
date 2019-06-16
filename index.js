const express = require("express");
const app = express();
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

String.prototype.replaceAll = function(search, replacement) {
  var target = this;
  return target.replace(new RegExp(search, "g"), replacement);
};
let runPy = (hand = "3cAh3dThJs") =>
  new Promise(function(resolve, reject) {
    const { spawn } = require("child_process");
    const vpAnalyzer = spawn("python", [`./vp_analyzer.py`, hand]);

    vpAnalyzer.stdout.on("data", function(data) {
      console.log("TCL: data", data.toString());
      resolve(data.toString());
    });

    vpAnalyzer.stderr.on("data", data => {
      console.log("TCL: data", data.toString());
      reject(data.toString());
    });
  });

app.get("*", (req, res) => {
  runPy(req.path.replace("/", ""))
    .then(function(fromRunpy) {
      const temp = fromRunpy.replaceAll("'", '"');
      console.log("TCL: temp", temp);
      res.json(JSON.parse(temp));
    })
    .catch(e => {
      res.json(e);
    });
});

app.listen(4000, () => console.log("Application listening on port 4000!"));
