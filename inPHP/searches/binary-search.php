<?php
function binary_search($n, $x) {
    $i = 0;
    $d = len(n) - 1;

    while ($i < len(n)) {
        $mid_val = $i + ($d - 1) / 2;
        if ($n[$mid_val] == $x) {
            return $mid_val;
        }
        elseif ($n[$mid_val] < $x) {
            $i = $mid_val + 1;
        }
        else {
            $i = $center - 1;
        }
    }
    return 'Position not found';
}
$sorted = [52,3,4,5,6,456,24,546,68,23,1,78,0,-1,32];
print(binary_search($sorted, 546));
?>