import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Production of Cocoa.csv")

df["Year"] = df["Year"].astype(str)

df_ivory = df[df["Area"]=="Côte d'Ivoire"].drop(columns=["Area"])
df_ghana = df[df["Area"]=="Ghana"].drop(columns=["Area"])

def plot_scatter(country_df, country_name, color="purple"):
    fig, ax = plt.subplots(figsize=(11,6))
    ax.scatter(country_df["Year"], country_df["Yield"], color=color)
    ax.set_title(f"year vs yield - {country_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Yield")
    ax.set_xticks(country_df["Year"])
    ax.set_xticklabels(country_df["Year"], rotation=90)
    ax.grid(True)
    plt.show()

def plot_bar(country_df, country_name, color="pink"):
    fig, ax = plt.subplots(figsize=(11,6))
    ax.bar(country_df["Year"], country_df["Area harvested"], color=color)
    ax.set_title(f"Area harvested by year- {country_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Area harvested")
    ax.set_xticks(country_df["Year"])
    ax.set_xticklabels(country_df["Year"], rotation=90)
    ax.grid(axis="y")
    plt.show()

fig, ax = plt.subplots(2,2, figsize=(14,7))
if isinstance(ax, plt.Axes):
    ax = [ax]
else:
    ax = ax.flatten()

#Panel 1
ax[0].scatter(df_ghana["Year"], df_ghana["Yield"], color="purple")
ax[0].set_title("Ghana - Year vs Yield ")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Yield")
ax[0].grid(True)
ax[0].tick_params(axis='x', rotation=90)

#Panel 2
ax[1].scatter(df_ivory["Year"], df_ivory["Yield"], color="brown")
ax[1].set_title("Côte d'Ivoire - Year vs Yield ")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Yield")
ax[1].grid(True)
ax[1].tick_params(axis='x', rotation=90)

#panel 3
ax[2].bar(df_ghana["Year"], df_ghana["Area harvested"], color="pink")
ax[2].set_title("Ghana - Area harvested by year")
ax[2].set_xlabel("Year")
ax[2].set_ylabel("Area harvested")
ax[2].grid(axis="y")
ax[2].tick_params(axis='x', rotation=90)

#panel 4
ax[3].bar(df_ivory["Year"], df_ivory["Area harvested"], color="gold")
ax[3].set_title("Côte d'Ivoire - Area harvested by year")
ax[3].set_xlabel("Year")
ax[3].set_ylabel("Area harvested")
ax[3].grid(axis="y")
ax[3].tick_params(axis='x', rotation=90)

fig.suptitle("Cocoa Production Analysis", fontsize=16)
plt.tight_layout(rect= [0,0,1,0.96])
fig.savefig("Cocoa_study.pdf")
plt.show()



print("Côte d'Ivoire table.")
print(df_ivory)
print("Ghana table.")
print(df_ghana)
plot_scatter(df_ivory, "Côte d'Ivoire", color="brown")
plot_scatter(df_ghana, "Ghana", color="purple")
plot_bar(df_ivory, "Côte d'Ivoire", color="gold")
plot_bar(df_ghana, "Ghana", color="pink")