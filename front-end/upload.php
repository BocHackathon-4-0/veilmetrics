<?php

#$target_dir = "./";
$target_dir = "C:\Users\admin\Desktop\BOC Hackathon\code/";
$target_file = $target_dir . basename($_FILES["pdfFile"]["name"]);

if (file_exists($target_file)) {
    echo "Sorry, file already exists. ";
    exit;
}

if (move_uploaded_file($_FILES["pdfFile"]["tmp_name"], $target_file)) {
    echo "The file " . basename($_FILES["pdfFile"]["name"]) . " has been uploaded.";
} else {
    echo "Sorry, there was an error uploading your file.";
}

// "dates": ["06 Apr, 2022", "07 Apr, 2022", "08 Apr, 2022", "09 Apr, 2022", "10 Apr, 2022", "11 Apr, 2022", "12 Apr, 2022", "13 Apr, 2022", "14 Apr, 2022", "15 Apr, 2022", "16 Apr, 2022", "17 Apr, 2022", "18 Apr, 2022", "19 Apr, 2022", "20 Apr, 2022", "21 Apr, 2022", "22 Apr, 2022", "23 Apr, 2022", "24 Apr, 2022", "25 Apr, 2022", "26 Apr, 2022", "27 Apr, 2022", "28 Apr, 2022", "29 Apr, 2022", "30 Apr, 2022", "01 May, 2022", "02 May, 2022", "03 May, 2022", "04 May, 2022", "05 May, 2022", "06 May, 2022", "07 May, 2022", "08 May, 2022", "09 May, 2022", "10 May, 2022", "11 May, 2022", "12 May, 2022", "13 May, 2022", "14 May, 2022", "15 May, 2022", "16 May, 2022", "17 May, 2022", "18 May, 2022", "19 May, 2022", "20 May, 2022", "21 May, 2022", "22 May, 2022", "23 May, 2022", "24 May, 2022", "25 May, 2022", "26 May, 2022", "27 May, 2022", "28 May, 2022", "29 May, 2022", "30 May, 2022", "31 May, 2022", "01 Jun, 2022", "02 Jun, 2022", "03 Jun, 2022", "04 Jun, 2022", "05 Jun, 2022", "06 Jun, 2022", "07 Jun, 2022", "08 Jun, 2022", "09 Jun, 2022", "10 Jun, 2022", "11 Jun, 2022", "12 Jun, 2022", "13 Jun, 2022", "14 Jun, 2022", "15 Jun, 2022", "16 Jun, 2022", "17 Jun, 2022", "18 Jun, 2022", "19 Jun, 2022", "20 Jun, 2022", "21 Jun, 2022", "22 Jun, 2022", "23 Jun, 2022", "24 Jun, 2022", "25 Jun, 2022", "26 Jun, 2022", "27 Jun, 2022", "28 Jun, 2022", "29 Jun, 2022", "30 Jun, 2022", "01 Jul, 2022", "02 Jul, 2022", "03 Jul, 2022", "04 Jul, 2022", "05 Jul, 2022", "06 Jul, 2022", "07 Jul, 2022", "08 Jul, 2022", "09 Jul, 2022", "10 Jul, 2022", "11 Jul, 2022", "12 Jul, 2022", "13 Jul, 2022", "14 Jul, 2022", "15 Jul, 2022", "16 Jul, 2022", "17 Jul, 2022", "18 Jul, 2022", "19 Jul, 2022", "20 Jul, 2022", "21 Jul, 2022", "22 Jul, 2022", "23 Jul, 2022", "24 Jul, 2022", "25 Jul, 2022", "26 Jul, 2022", "27 Jul, 2022", "28 Jul, 2022", "29 Jul, 2022", "30 Jul, 2022", "31 Jul, 2022", "01 Aug, 2022", "02 Aug, 2022", "03 Aug, 2022", "04 Aug, 2022", "05 Aug, 2022", "06 Aug, 2022", "07 Aug, 2022", "08 Aug, 2022", "09 Aug, 2022", "10 Aug, 2022", "11 Aug, 2022", "12 Aug, 2022", "13 Aug, 2022", "14 Aug, 2022", "15 Aug, 2022", "16 Aug, 2022", "17 Aug, 2022", "18 Aug, 2022", "19 Aug, 2022", "20 Aug, 2022", "21 Aug, 2022", "22 Aug, 2022", "23 Aug, 2022", "24 Aug, 2022", "25 Aug, 2022", "26 Aug, 2022", "27 Aug, 2022", "28 Aug, 2022", "29 Aug, 2022", "30 Aug, 2022", "31 Aug, 2022", "01 Sep, 2022", "02 Sep, 2022", "03 Sep, 2022", "04 Sep, 2022", "05 Sep, 2022", "06 Sep, 2022", "07 Sep, 2022", "08 Sep, 2022", "09 Sep, 2022", "10 Sep, 2022", "11 Sep, 2022", "12 Sep, 2022", "13 Sep, 2022", "14 Sep, 2022", "15 Sep, 2022", "16 Sep, 2022", "17 Sep, 2022", "18 Sep, 2022", "19 Sep, 2022", "20 Sep, 2022", "21 Sep, 2022", "22 Sep, 2022", "23 Sep, 2022", "24 Sep, 2022", "25 Sep, 2022", "26 Sep, 2022", "27 Sep, 2022", "28 Sep, 2022", "29 Sep, 2022", "30 Sep, 2022", "01 Oct, 2022", "02 Oct, 2022", "03 Oct, 2022", "04 Oct, 2022", "05 Oct, 2022", "06 Oct, 2022", "07 Oct, 2022", "08 Oct, 2022", "09 Oct, 2022", "10 Oct, 2022", "11 Oct, 2022", "12 Oct, 2022", "13 Oct, 2022", "14 Oct, 2022", "15 Oct, 2022", "16 Oct, 2022", "17 Oct, 2022", "18 Oct, 2022", "19 Oct, 2022", "20 Oct, 2022", "21 Oct, 2022", "22 Oct, 2022", "23 Oct, 2022", "24 Oct, 2022", "25 Oct, 2022", "26 Oct, 2022", "27 Oct, 2022", "28 Oct, 2022", "29 Oct, 2022", "01 Nov, 2022", "02 Nov, 2022", "03 Nov, 2022", "04 Nov, 2022", "05 Nov, 2022", "06 Nov, 2022", "07 Nov, 2022", "08 Nov, 2022", "09 Nov, 2022", "10 Nov, 2022", "11 Nov, 2022", "12 Nov, 2022", "13 Nov, 2022", "14 Nov, 2022", "15 Nov, 2022", "16 Nov, 2022", "17 Nov, 2022", "18 Nov, 2022", "19 Nov, 2022", "20 Nov, 2022", "21 Nov, 2022", "22 Nov, 2022", "23 Nov, 2022", "24 Nov, 2022", "25 Nov, 2022", "26 Nov, 2022", "27 Nov, 2022", "28 Nov, 2022", "29 Nov, 2022", "30 Nov, 2022", "01 Dec, 2022", "02 Dec, 2022", "03 Dec, 2022", "04 Dec, 2022", "05 Dec, 2022", "06 Dec, 2022", "07 Dec, 2022", "08 Dec, 2022", "09 Dec, 2022", "10 Dec, 2022", "11 Dec, 2022", "12 Dec, 2022", "13 Dec, 2022", "14 Dec, 2022", "15 Dec, 2022", "16 Dec, 2022", "17 Dec, 2022", "18 Dec, 2022", "19 Dec, 2022", "20 Dec, 2022", "21 Dec, 2022", "22 Dec, 2022", "23 Dec, 2022", "24 Dec, 2022", "25 Dec, 2022", "26 Dec, 2022", "27 Dec, 2022", "28 Dec, 2022", "29 Dec, 2022", "30 Dec, 2022", "31 Dec, 2022", "01 Jan, 2023", "02 Jan, 2023", "03 Jan, 2023", "04 Jan, 2023", "05 Jan, 2023", "06 Jan, 2023", "07 Jan, 2023", "08 Jan, 2023", "09 Jan, 2023", "10 Jan, 2023", "11 Jan, 2023", "12 Jan, 2023", "13 Jan, 2023", "14 Jan, 2023", "15 Jan, 2023", "16 Jan, 2023", "17 Jan, 2023", "18 Jan, 2023", "19 Jan, 2023", "20 Jan, 2023", "21 Jan, 2023", "22 Jan, 2023", "23 Jan, 2023", "24 Jan, 2023", "25 Jan, 2023", "26 Jan, 2023", "27 Jan, 2023", "28 Jan, 2023", "29 Jan, 2023", "30 Jan, 2023", "31 Jan, 2023", "01 Feb, 2023", "02 Feb, 2023", "03 Feb, 2023", "04 Feb, 2023", "05 Feb, 2023", "06 Feb, 2023", "07 Feb, 2023", "08 Feb, 2023", "09 Feb, 2023", "10 Feb, 2023", "11 Feb, 2023", "12 Feb, 2023", "13 Feb, 2023", "14 Feb, 2023", "15 Feb, 2023", "16 Feb, 2023", "17 Feb, 2023", "18 Feb, 2023", "19 Feb, 2023", "20 Feb, 2023", "21 Feb, 2023", "22 Feb, 2023", "23 Feb, 2023", "24 Feb, 2023", "25 Feb, 2023", "26 Feb, 2023", "27 Feb, 2023", "01 Mar, 2023", "02 Mar, 2023", "03 Mar, 2023", "04 Mar, 2023", "05 Mar, 2023", "06 Mar, 2023", "07 Mar, 2023", "08 Mar, 2023", "09 Mar, 2023", "10 Mar, 2023", "11 Mar, 2023", "12 Mar, 2023", "13 Mar, 2023", "14 Mar, 2023", "15 Mar, 2023", "16 Mar, 2023", "17 Mar, 2023", "18 Mar, 2023", "19 Mar, 2023", "20 Mar, 2023", "21 Mar, 2023", "22 Mar, 2023", "23 Mar, 2023", "24 Mar, 2023", "25 Mar, 2023", "26 Mar, 2023", "27 Mar, 2023", "28 Mar, 2023", "29 Mar, 2023", "30 Mar, 2023", "31 Mar, 2023", "01 Apr, 2023", "02 Apr, 2023", "03 Apr, 2023", "04 Apr, 2023", "05 Apr, 2023", "06 Apr, 2023", "07 Apr, 2023", "08 Apr, 2023", "09 Apr, 2023", "10 Apr, 2023", "11 Apr, 2023", "12 Apr, 2023", "13 Apr, 2023", "14 Apr, 2023", "15 Apr, 2023", "16 Apr, 2023", "17 Apr, 2023", "18 Apr, 2023", "19 Apr, 2023", "20 Apr, 2023", "21 Apr, 2023", "22 Apr, 2023", "23 Apr, 2023", "24 Apr, 2023", "25 Apr, 2023", "26 Apr, 2023", "27 Apr, 2023", "28 Apr, 2023", "29 Apr, 2023", "01 Jun, 2023", "02 Jun, 2023", "03 Jun, 2023", "04 Jun, 2023", "05 Jun, 2023", "06 Jun, 2023"]}

?>