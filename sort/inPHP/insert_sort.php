<?php
/* Insert sort PHP implementation
   Complexity: 0(n^2)
   Emmanuel Bashorun. 2019.
*/

function insert_sort($sort) {
    $value = 0;
    $arrHolder = array();
    while ($value < count($sort)) {
        $arrHolder[] = $value;
        $value++;
    }
    
    foreach ($arrHolder as $j) {
        $key = $sort[$j];
        $index = $j;

        while ($index > 0 AND $sort[$index - 1] > $key) {
            $sort[$index] = $sort[$index - 1];
            $index = $index - 1;  
        }
        $sort[$index] = $key;
    }
    foreach($sort as $i) {
        echo $i . ', ';
    }
    return $sort;
    
}
echo "[5, 2, 6, 4, 1, 3] <br />";
insert_sort([5, 2, 6, 4, 1, 3]);
?>
