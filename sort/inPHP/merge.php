<?php
function merge_sort($arr) {
   if (count($arr) <= 1) {
       return $arr;
   }
   $mid = count($arr) / 2;
   $left = merge_sort(array_slice($arr, $mid));
   $right = merge_sort(array_slice($arr, 0, $mid));
    
   return merge($left, $right);

}

function merge($left, $right) {
    $arr = array();
    $left_cursor = 0;
    $right_cursor = 0;

    while ($left_cursor < count($left) AND $right_cursor < count($right)) {
        if ($left[$left_cursor] <= $right[$right_cursor]) {
            $arr = $left[$left_cursor];
            $left_cursor += 1;
        }
        else {
            $arr = $right[$right_cursor];
            $right_cursor += 1;
        }
    }
    for ($i; $i = getRange($left_cursor, $left); ++$i) {
        $arr = $left[$i];    
    }
    for ($i; $i = getRange($right_cursor, $right); ++$i) {
        $arr = $right[$i];
    }

    return $arr;
}

function getRange($val, $sort) {
    $arrHolder = array();
    while ($val < count($sort)) {
        $arrHolder[] = $val;
        $val++;
    }

    return $arrHolder;
}

$array = [1,5,7,4,3,2,1,9,0,10,43,64];
print_r(merge_sort($array));

?>