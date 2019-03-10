<?php

$out = array();

$msg = $_GET['msg'];

$msg = str_replace("*-*"," ",$msg);

$value = "name1.py ".$msg;

$command = escapeshellcmd($value);

$output = exec($command,$out,$result);

$i=0;
foreach($out as $line) {
	//if($i>5){
		 echo $line;
	//}
    //$i++;
}


?>