

## Spotify Listening Data Dashboard

This project is a lightweight interactive dashboard for visualizing Spotify listening data.

The application loads a predefined dataset derived from Spotify listening history and presents it through interactive charts and summaries. The goal is to make patterns in listening behavior easier to explore without needing to manually inspect raw data files.



The dashboard is built with Gradio, allowing the interface and visualizations to be served directly from Python.



## Link to dataset 

https://www.kaggle.com/datasets/dhruvildave/spotify-charts



### Purpose

Spotify listening exports contain a large amount of useful information about listening habits, but the raw data is difficult to interpret at a glance. This project converts that structured dataset into visual summaries that highlight trends such as listening frequency, artist popularity, and track activity over time.

### Design Philosophy

The application is designed around a fixed dataset structure rather than accepting arbitrary CSV uploads.

Supporting any possible CSV format would require complex schema detection, data cleaning, and interpretation logic. Instead, the dashboard focuses on presenting meaningful insights from a known dataset generated from Spotify listening history.

This allows the project to remain simple, stable, and focused on visualization.

### Features

Visual summaries of listening history

Artist and track frequency analysis

Time-based listening trends

Interactive dashboard controls for exploring the dataset

### Tech Stack

Python

Gradio

Data visualization libraries (e.g., Matplotlib / Plotly)

Preprocessed Spotify listening dataset (CSV)

## Project Goal

The goal of this project is to turn raw Spotify listening data into a clear and interactive dashboard. By focusing on a predefined dataset structure, the project emphasizes useful visualizations rather than complex data ingestion systems.