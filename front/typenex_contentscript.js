var arrayOfNumbers = [];
alert("hi");
var regex =  /\d*[/-]*[0-9][0-9][0-9][/ -]*[0-9][0-9][0-9][/ -]*[0-9][0-9][0-9][0-9][ ]*/g;
newBody = document.body.innerHTML;
var i = 0;
do
{
    temp = regex.exec(newBody);
    if (temp != null)
        arrayOfNumbers[i] = temp;
    i++
}
while (temp)
for (var i = 0; i < arrayOfNumbers.length; i++)
{
    newBody = newBody.replace(arrayOfNumbers[i], "<a href='http://www.google.com'>" + arrayOfNumbers[i] + "</a>");
}
document.body.innerHTML = newBody;