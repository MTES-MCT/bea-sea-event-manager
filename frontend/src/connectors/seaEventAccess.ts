import { SeaEventFormLine } from "@/model/SeaEventFormLine";
import { SeaEventSummary } from "@/model/SeaEventSummary";

export function registerSeaEventForm(
  seaEventFormData: SeaEventFormLine[]
): void {
  console.log("registerSeaEventForm called with", seaEventFormData);
}

export function archiveSeaEvent(seaEventUUID: string): void {
  console.log("archiveSeaEvent called with", seaEventUUID);
}

export function getSeaEventFormData(seaEventUUID: string): SeaEventFormLine[] {
  const seaEventDemo: {
    [key: string]: any;
  } = {
    "123141-12312-12312-123131": <SeaEventFormLine[]>[
      {
        name: "Nom du navire",
        initialReportValue: "IBIS (FRANCE)",
        referenceValue: "IBIS 2(FRANCE)",
        defaultSelectedValue: "",
      },
      {
        name: "IMO ",
        initialReportValue: "1234567",
        referenceValue: "1234567",
        defaultSelectedValue: "",
      },
      {
        name: "Indicatif",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Pavillon",
        initialReportValue: "France",
        referenceValue: "France",
        defaultSelectedValue: "",
      },
      {
        name: "Numéro d'immatriculation",
        initialReportValue: "987654",
        referenceValue: "987654",
        defaultSelectedValue: "",
      },
      {
        name: "Jauge brute",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Année de construction",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Longueur totale",
        initialReportValue: "",
        referenceValue: "154 m",
        defaultSelectedValue: "",
      },
      {
        name: "Matériau de la coque",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Type de propulsion",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Type de navire / embarcation",
        initialReportValue: "navire à passagers",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Numéro national événement",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Date de l'événement",
        initialReportValue: "9 mars 22",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Titre de l'événement",
        initialReportValue: "collision",
        referenceValue: "collision",
        defaultSelectedValue: "",
      },
      {
        name: "Date de notification",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Heure de notification",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Entité de notification",
        initialReportValue: "CROSS Jobourg",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Directive 2009/18",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Latitude",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Longitude",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Etat côtiers aff.",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Zone maritime de l'événement",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Localisation national ",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
    ],
    "123141-12312-12312-123133": <SeaEventFormLine[]>[
      {
        name: "Nom du navire",
        initialReportValue: "moineau_1",
        referenceValue: "moineau_2",
        defaultSelectedValue: "",
      },
      {
        name: "Imo ",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Indicatif",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Etat",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Numéro d'immatriculation",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Jauge brute",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Année de construction",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Longueur totale",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Matériau de la coque",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Type de propulsion",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Type de navire / embarcation",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Numéro national événement",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Date de l'événement",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Titre de l'événement",
        initialReportValue: "incendie",
        referenceValue: "incendie",
        defaultSelectedValue: "",
      },
      {
        name: "Date de notification",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Heure de notification",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Entité de notification",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Directive 2009/18",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Latitude",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Longitude",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Etat côtiers aff.",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Zone maritime de l'événement",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
      {
        name: "Localisation national ",
        initialReportValue: "",
        referenceValue: "",
        defaultSelectedValue: "",
      },
    ],
  };
  return seaEventDemo[seaEventUUID];
}
