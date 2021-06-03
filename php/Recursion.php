<?php
function fact($data){
    if($data==1){
        return 1;
    }
    else
    return $data*fact($data-1);
}
echo fact(5);
?>