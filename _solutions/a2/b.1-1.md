---
layout: clrs-solution
title:  "Exercise B.1-1"
---
>Draw Venn diagrams that illustrate the first of the distributive laws (B.1).

$$A \cap (B \cup C) = ( A \cap B ) \cup (A \cap C)$$

![B.1-1 Venn Diagram a]({{ '/assets/img/B-1-1-a.png' | prepend: site.baseurl }}){:class="latex-img"}

$$=$$

![B.1-1 Venn Diagram b]({{ '/assets/img/B-1-1-b.png' | prepend: site.baseurl }}){:class="latex-img"}

$$=$$

![B.1-1 Venn Diagram c]({{ '/assets/img/B-1-1-c.png' | prepend: site.baseurl }}){:class="latex-img"}



The following LaTeX code was used to generate Venn diagram $$A$$:

{% highlight latex %}
\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
    \begin{tikzpicture}[
dot/.style = {circle, inner sep=0pt, minimum size=1mm, fill,
              node contents={}}
                        ]
\def\firstcircle{(-1.2,0) coordinate (a) circle (2cm)}
\def\secondcircle{(1.2,0) coordinate (b)  circle (2cm)}
\def\thirdcircle{(0,-2.0) coordinate (c) circle (2cm)}
    \begin{scope}
\fill[gray] \firstcircle;
    \end{scope}
\draw \firstcircle  node[text=black,above] {$A$};
\draw \secondcircle node[text=black,above] {$B$}; 
\draw \thirdcircle node[text=black,below] {$C$};
\node [below=4cm, align=flush center,text width=8cm]
        {
            $A$
        };
    \end{tikzpicture}
  \end{document}
{% endhighlight %}

The following LaTeX code was used to generate Venn diagram $$B \cap C$$:

{% highlight latex %}
\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
    \begin{tikzpicture}[
dot/.style = {circle, inner sep=0pt, minimum size=1mm, fill,
              node contents={}}
                        ]
\def\firstcircle{(-1.2,0) coordinate (a) circle (2cm)}
\def\secondcircle{(1.2,0) coordinate (b)  circle (2cm)}
\def\thirdcircle{(0,-2.0) coordinate (c) circle (2cm)}
    \begin{scope}
\fill[gray] \secondcircle;
\fill[gray] \thirdcircle;
    \end{scope}
\draw \firstcircle  node[text=black,above] {$A$};
\draw \secondcircle node[text=black,above] {$B$}; 
\draw \thirdcircle node[text=black,below] {$C$};
\node [below=4cm, align=flush center,text width=8cm]
        {
            $B \cup C$
        };
    \end{tikzpicture}
  \end{document}
{% endhighlight %}

The following LaTeX code was used to generate Venn diagram $$A \cap (B \cup C)$$:

{% highlight latex %}

\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
    \begin{tikzpicture}[
dot/.style = {circle, inner sep=0pt, minimum size=1mm, fill,
              node contents={}}
                        ]
\def\firstcircle{(-1.2,0) coordinate (a) circle (2cm)}
\def\secondcircle{(1.2,0) coordinate (b)  circle (2cm)}
\def\thirdcircle{(0,-2.0) coordinate (c) circle (2cm)}
     \begin{scope}
    \clip \secondcircle;
    \fill[gray] \firstcircle;
      \end{scope}
      \begin{scope}
    \clip \firstcircle;
    \fill[gray] \thirdcircle;
      \end{scope}
\draw \firstcircle  node[text=black,above] {$A$};
\draw \secondcircle node[text=black,above] {$B$}; 
\draw \thirdcircle node[text=black,below] {$C$};
\node [below=4cm, align=flush center,text width=8cm]
        {
            $A \cap (B \cup C)$
        };
    \end{tikzpicture}
  \end{document}
{% endhighlight %}

The following LaTeX code was used to generate Venn diagram $$A \cap B$$:

{% highlight latex %}
\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
    \begin{tikzpicture}[
dot/.style = {circle, inner sep=0pt, minimum size=1mm, fill,
              node contents={}}
                        ]
\def\firstcircle{(-1.2,0) coordinate (a) circle (2cm)}
\def\secondcircle{(1.2,0) coordinate (b)  circle (2cm)}
\def\thirdcircle{(0,-2.0) coordinate (c) circle (2cm)}
     \begin{scope}
    \clip \secondcircle;
    \fill[gray] \firstcircle;
      \end{scope}
\draw \firstcircle  node[text=black,above] {$A$};
\draw \secondcircle node[text=black,above] {$B$}; 
\draw \thirdcircle node[text=black,below] {$C$};
\node [below=4cm, align=flush center,text width=8cm]
        {
            $A \cap B$
        };
    \end{tikzpicture}
  \end{document}
{% endhighlight %}

The following LaTeX code was used to generate Venn diagram $$A \cap C$$:

{% highlight latex %}
\documentclass[tikz, margin=3mm]{standalone}

\begin{document}
    \begin{tikzpicture}[
dot/.style = {circle, inner sep=0pt, minimum size=1mm, fill,
              node contents={}}
                        ]
\def\firstcircle{(-1.2,0) coordinate (a) circle (2cm)}
\def\secondcircle{(1.2,0) coordinate (b)  circle (2cm)}
\def\thirdcircle{(0,-2.0) coordinate (c) circle (2cm)}
     \begin{scope}
    \clip \thirdcircle;
    \fill[gray] \firstcircle;
      \end{scope}
\draw \firstcircle  node[text=black,above] {$A$};
\draw \secondcircle node[text=black,above] {$B$}; 
\draw \thirdcircle node[text=black,below] {$C$};
\node [below=4cm, align=flush center,text width=8cm]
        {
            $A \cap C$
        };
    \end{tikzpicture}
  \end{document}

  {% endhighlight %}