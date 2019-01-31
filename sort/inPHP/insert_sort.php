<?php
function insertion_sort($arr) {
    $value = 0;
    $arrHolder = array();
    while ($value < count($arr)) {
        $arrHolder[] = $value;
        $value++;
    }
    
    foreach ($arrHolder as $i => $j) {
        $cursor = $arr[$j];
        $pos = $j;

        while ($pos > 0 AND $arr[$pos - 1] > $cursor) {
            $arr[$pos] = $arr[$pos - 1];
            $pos = $pos - 1;  
        }
        $arr[$pos] = $cursor;
    }
    return $arr;
}
print_r(insertion_sort([5, 2, 6, 4, 1, 55, 3, 7, 8, 19, 9, 21, 13, 456, 9133234, 212, 87, 17, 11]));

?>